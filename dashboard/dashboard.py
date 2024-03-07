# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns

# Setting Layout
st.set_page_config(layout="wide")

# Import Dataframe
day_df = pd.read_csv("../data/day.csv")
hour_df = pd.read_csv("../data/hour.csv")
bike_df = pd.read_csv("../data/day_clean.csv")

# Change the Data Type of the "dteday" Column 
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Visualisasi pertama
def visualisasi_pertama():
    st.header("Berapa rata-rata jumlah persewaan sepeda per jam dan bagaimana variasinya sepanjang hari?")
    plt.figure(figsize=(10, 5))
    sns.barplot(
        y="cnt",
        x="hr",
        data=hour_df.sort_values(by="hr", ascending=False),
    )
    plt.title("Jumlah Bike Sharing Berdasarkan Jam", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis="x", labelsize=12)
    st.pyplot(plt)

# Visualisasi kedua
def visualisasi_kedua():
    st.header("Berapa rata-rata jumlah persewaan sepeda per bulan dan bagaimana variasinya sepanjang bulan?")

    plt.figure(figsize=(10, 5))
    sns.barplot(y="cnt",x="mnth",data=day_df.sort_values(by="mnth", ascending=False))
    plt.title("Jumlah Bike Sharing Berdasarkan Bulan", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis="x", labelsize=12)
    st.pyplot(plt)

# Visualisasi ketiga
def visualisasi_ketiga():
    st.header("Berapa rata-rata jumlah persewaan sepeda per Tahun dan bagaimana variasinya sepanjang Tahun?")

    yearly_df = day_df.resample("Y", on="dteday").sum()
    yearly_df = yearly_df.reset_index()
    yearly_df["dteday"] = ["2011", "2012"]

    plt.figure(figsize=(16, 8))
    plt.bar(yearly_df["dteday"], yearly_df["cnt"])

    for i in range(len(yearly_df["dteday"])):
        plt.text(i, yearly_df["cnt"][i],
                str(yearly_df["cnt"][i]),
                ha="center", va="bottom")

    plt.title("Bike Rental Trends by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Bike Rentals")

    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

# Visualisasi keempat
def visualisasi_keempat():
    st.header("Bagaimana hubungan kondisi cuaca memengaruhi rata-rata persewaan sepeda?")

    avg_weather = bike_df.groupby('weather_label')['cnt_day'].mean().reset_index().sort_values("cnt_day")

    plt.figure(figsize=(10, 6))
    sns.barplot(x='cnt_day', y='weather_label', data=avg_weather, hue='weather_label', palette='viridis', legend=False)

    plt.title('Rata - Rata Penyewaan Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Rata - Rata Penyewaan')
    plt.ylabel('Kondisi Cuaca')

    st.pyplot(plt)

# Visualisasi kelima
def visualisasi_kelima():
    st.header("Bagaimana hubungan hari libur memengaruhi kenaikan atau penurunan rata-rata persewaan?")
    avg_holiday = bike_df.groupby('holiday_day')['cnt_day'].mean().reset_index().sort_values("cnt_day")

    plt.figure(figsize=(8, 5))
    sns.barplot(x='holiday_day', y='cnt_day', data=avg_holiday, hue='holiday_day', palette='Set2', legend=False)

    plt.title('Rata-rata Penyewaan Sepeda pada Hari Libur')
    plt.xlabel('Hari Libur')
    plt.ylabel('Rata-rata Penyewaan')
    plt.xticks([0, 1], ['Tidak Libur', 'Libur'])

    st.pyplot(plt)

# Streamlit app
def main():
    st.title("Visualisasi Data Bike Sharing")

    # Create tabs
    tab = st.selectbox("Pilih Visualisasi:", ("Bike Rental Trends by Hour", "Bike Rental Trends by Month", "Bike Rental Trends by Year", "Bike Rental Trends by Weather", "Bike Rentals by Holidays and Not Holiday"))

    if tab == "Bike Rental Trends by Hour":
        visualisasi_pertama()
    elif tab == "Bike Rental Trends by Month":
        visualisasi_kedua()
    elif tab == "Bike Rental Trends by Year":
        visualisasi_ketiga()
    elif tab == "Bike Rental Trends by Weather":
        visualisasi_keempat()
    elif tab == "Bike Rentals by Holidays and Not Holiday":
        visualisasi_kelima()

if __name__ == "__main__":
    main()