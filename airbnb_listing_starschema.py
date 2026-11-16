import os
import pandas as pd


def create_star_schema(
    input_csv_path, output_dir=os.path.join("dataset", "parquet_output")
):
    print(f" Membaca data dari '{input_csv_path}'...")
    df = pd.read_csv(input_csv_path)

    # 1. Formatting tipe data kunci & tanggal
    if "listing_id" in df.columns:
        df["listing_id"] = df["listing_id"].astype(str)
    if "host_id" in df.columns:
        df["host_id"] = df["host_id"].astype(str)
    if "month_date" in df.columns:
        df["month_date"] = pd.to_datetime(df["month_date"])
        # Urutkan berdasarkan tanggal agar entri terbaru berada di posisi paling bawah
        df = df.sort_values("month_date")

    print(" Memproses pembentukan Star Schema...")

    # ----------------------------------------------------
    # A. TABEL DIMENSI: HOST (Ambil status superhost terbaru)
    # ----------------------------------------------------
    host_cols = [c for c in ["host_id", "superhost"] if c in df.columns]
    dim_host = (
        df[host_cols]
        .drop_duplicates(subset=["host_id"], keep="last")
        .reset_index(drop=True)
    )

    # ----------------------------------------------------
    # B. TABEL DIMENSI: LISTING (Master Properti & Lokasi)
    # ----------------------------------------------------
    dim_listing_cols = [
        "listing_id",
        "host_id",
        "listing_type",
        "room_type",
        "property_type",
        "country",
        "currency",
        "neighborhood",
        "latitude",
        "longitude",
        "guests",
        "bedrooms",
        "beds",
        "baths",
    ]
    existing_listing_cols = [c for c in dim_listing_cols if c in df.columns]
    dim_listing = (
        df[existing_listing_cols]
        .drop_duplicates(subset=["listing_id"], keep="last")
        .reset_index(drop=True)
    )

    # ----------------------------------------------------
    # C. TABEL FAKTA: PERFORMANCE (Metrik Kinerja Bulanan)
    # ----------------------------------------------------
    fact_performance_cols = [
        "listing_id",
        "month_date",
        "active",
        "available_days",
        "unavailable_days",
        "occupancy",
        "avg_daily_rate",
        "native_avg_daily_rate",
        "revenue",
        "native_revenue",
        "revpar",
        "native_revpar",
        "num_reviews",
        "star_rating",
        "booking_lead_time_avg",
        "length_of_stay_avg",
        "booked_rate_avg",
    ]
    existing_fact_cols = [c for c in fact_performance_cols if c in df.columns]
    fact_performance = df[existing_fact_cols].reset_index(drop=True)

    # ----------------------------------------------------
    # D. EKSPOR KE FORMAT PARQUET (Engine: PyArrow)
    # ----------------------------------------------------
    os.makedirs(output_dir, exist_ok=True)

    host_path = os.path.join(output_dir, "dim_host.parquet")
    listing_path = os.path.join(output_dir, "dim_listing.parquet")
    fact_path = os.path.join(output_dir, "fact_performance.parquet")

    dim_host.to_parquet(host_path, index=False, engine="pyarrow")
    dim_listing.to_parquet(listing_path, index=False, engine="pyarrow")
    fact_performance.to_parquet(fact_path, index=False, engine="pyarrow")

    print("\n Ekspor Parquet Selesai!")
    print(
        f" |- {host_path} -> {dim_host.shape[0]:,} baris, {dim_host.shape[1]} kolom"
    )
    print(
        f" |- {listing_path} -> {dim_listing.shape[0]:,} baris, {dim_listing.shape[1]} kolom"
    )
    print(
        f" |- {fact_path} -> {fact_performance.shape[0]:,} baris, {fact_performance.shape[1]} kolom"
    )


if __name__ == "__main__":
    INPUT_FILE = os.path.join("dataset", "airbnb_listing_clean.csv")

    if os.path.exists(INPUT_FILE):
        create_star_schema(INPUT_FILE)
    else:
        print(f" File '{INPUT_FILE}' tidak ditemukan. Cek folder 'dataset/'.")