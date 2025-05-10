# LAPORAN PROYEK MACHINE LEARNING: PREDIKSI RISIKO DIABETES

## 1. Domain Proyek
Diabetes merupakan penyakit metabolik kronis yang sangat umum dan dapat menyebabkan komplikasi serius seperti gagal ginjal, penyakit jantung, hingga kebutaan jika tidak terdeteksi dan ditangani lebih awal. Menurut WHO, jumlah penderita diabetes meningkat secara signifikan setiap tahunnya dan menjadi salah satu penyebab kematian terbesar di dunia. Oleh karena itu, deteksi dini menjadi kunci pencegahan komplikasi lanjutan. 

Dalam proyek ini, kami membangun model machine learning untuk memprediksi kemungkinan seseorang menderita diabetes berdasarkan data medis sederhana.

**Referensi:**
- World Health Organization (WHO). (2023). Diabetes. https://www.who.int/news-room/fact-sheets/detail/diabetes
- UCI Machine Learning Repository: Pima Indians Diabetes Database. https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

---

## 2. Business Understanding

### Problem Statement
Bagaimana cara memprediksi risiko diabetes seseorang hanya dengan data pemeriksaan awal (seperti usia, kadar glukosa, tekanan darah) tanpa prosedur medis lanjutan?

### Goals
Membangun model klasifikasi yang mampu memprediksi apakah seseorang berisiko diabetes dengan akurasi dan interpretasi yang baik.

### Solution Statement
- Menggunakan dua algoritma machine learning: Logistic Regression dan Random Forest.
- Melakukan perbandingan performa antar algoritma.
- Menerapkan hyperparameter tuning untuk meningkatkan performa model Random Forest.

---

## 3. Data Understanding

Dataset yang digunakan adalah **Pima Indians Diabetes Dataset** dari Kaggle/UCI. Dataset terdiri dari 768 baris dan 9 kolom, dengan 8 fitur dan 1 label:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
- Outcome (0 = tidak diabetes, 1 = diabetes)

### Distribusi Target
- Tidak diabetes: ±500 entri
- Diabetes: ±200 entri

### Visualisasi dan Eksplorasi Data
- Korelasi antar fitur divisualisasikan menggunakan heatmap.
- Glucose dan BMI memiliki korelasi tinggi terhadap label (Outcome).
- Distribusi kelas divisualisasikan dengan countplot.

---

## 4. Data Preparation

### Pembersihan Data
- Nilai 0 pada kolom Glucose, BloodPressure, SkinThickness, Insulin, dan BMI diganti menjadi `NaN` karena tidak logis secara medis.
- Missing value diimputasi menggunakan **median** karena data tidak berdistribusi normal dan terdapat outlier.

### Normalisasi
- Fitur numerik dinormalisasi menggunakan `StandardScaler` agar model lebih cepat konvergen dan memiliki performa lebih baik.

### Split Data
- Data dibagi menjadi **80% data latih** dan **20% data uji** menggunakan `train_test_split`.
- Tujuannya untuk mengevaluasi performa model secara objektif.

---

## 5. Model Development

### Modeling

#### Model 1: Logistic Regression

##### Cara Kerja
Algoritma ini menggunakan fungsi logit (sigmoid) untuk memetakan input ke dalam probabilitas antara 0 dan 1. Model ini bekerja optimal jika hubungan antara fitur dan target bersifat linier.

##### Parameter
Menggunakan **default** parameter dari scikit-learn.

##### Kelebihan/Kekurangan (Opsional)
- Kelebihan: Cepat, sederhana, interpretatif.
- Kekurangan: Kurang optimal jika data bersifat non-linear.

---

#### Model 2: Random Forest

##### Cara Kerja
Random Forest adalah algoritma ensemble yang terdiri dari banyak decision tree. Model ini menggabungkan prediksi dari banyak pohon dengan voting untuk klasifikasi. Cocok untuk data dengan non-linearitas dan noise tinggi.

##### Parameter
- Awalnya digunakan parameter **default**.
- Kemudian dilakukan **hyperparameter tuning** dengan `GridSearchCV` pada:
  - `n_estimators`: 50, 100
  - `max_depth`: None, 5, 10
  - `min_samples_split`: 2, 5

##### Kelebihan/Kekurangan (Opsional)
- Kelebihan: Akurat, tidak mudah overfitting, dapat menangani missing value dan outlier.
- Kekurangan: Lebih lambat, kurang interpretatif.

---

### Feature Importance
Random Forest menunjukkan bahwa fitur paling penting adalah:
1. Glucose
2. BMI
3. Age

---

## 6. Evaluation

### Metrik Evaluasi
- **Accuracy**: (TP + TN) / Total
- **Precision**: TP / (TP + FP)
- **Recall**: TP / (TP + FN)
- **F1-score**: 2 * (Precision * Recall) / (Precision + Recall)

### Hasil Evaluasi
| Model                      | Accuracy | F1-score |
|----------------------------|----------|----------|
| Logistic Regression        | 75.32%   | 0.74     |
| Random Forest (default)    | 74.03%   | 0.73     |
| Random Forest (tuned)      | 76.62%   | 0.76     |

### Model Terbaik
Random Forest dengan tuning menunjukkan performa terbaik.

---

## 7. Kesimpulan

Model klasifikasi berbasis machine learning berhasil dibangun untuk memprediksi risiko diabetes. Data diproses secara sistematis, termasuk penanganan missing values, normalisasi, dan split data. Model terbaik (Random Forest dengan tuning) mencapai akurasi 76.62%.

Model ini dapat dijadikan alat skrining awal yang cepat, hemat biaya, dan tidak invasif untuk membantu tenaga medis mendeteksi risiko diabetes.

---

Disusun oleh:  
**David Kristian Silalahi**
