# Go-UMKM Recommendation API 🚀

API ini dibuat menggunakan **FastAPI** untuk memberikan **rekomendasi antara UMKM dan investor** berdasarkan profil mereka menggunakan model pembelajaran mesin yang telah dilatih dan dikonversi ke format **TensorFlow Lite (TFLite)**.

API ini **telah berhasil dideploy ke Heroku** dan siap digunakan dalam sistem frontend maupun backend.

---

## Teknologi yang Digunakan

- Python 3.10
- FastAPI
- TensorFlow Lite (tflite-runtime)
- Scikit-learn
- Pandas
- Joblib
- Heroku (deployment)

---

## Struktur Direktori

```

.
├── app/
│   ├── main.py                    # Entry point FastAPI
│   ├── model/
│   │   ├── recommender.py         # Model dan fungsi rekomendasi
│   │   ├── artifacts/             # Model dan preprocessor
│   │   │   ├── similarity\_model.tflite
│   │   │   └── preprocessor.joblib
│   │   └── data/
│   │       ├── investor\_data.csv
│   │       └── umkm\_data.csv
│   └── schemas/
│       └── request\_response.py    # Skema request
├── requirements.txt
├── Procfile                       # Untuk Heroku
├── .python-version

````

---

## 🚀 Deployment

API ini telah dideploy ke Heroku dan bisa langsung digunakan pada URL berikut:

**Base URL**:  
`https://umkm-fastapi-heroku-496b36a59a51.herokuapp.com`

---

## Endpoint

### GET `/`

Cek apakah API aktif.

**Contoh Response:**
```json
{
  "message": "Go-UMKM Recommendation API is running."
}
````

---

### GET `/recommend/{user_id}?k=5`

Mendapatkan rekomendasi pengguna dari jenis yang berlawanan berdasarkan kemiripan profil.

* **Path Parameter:**

  * `user_id`: UUID pengguna (UMKM atau investor)
* **Query Parameter:**

  * `k`: Jumlah hasil rekomendasi (default: 5)

**Contoh Request:**

```
GET https://umkm-fastapi-heroku-496b36a59a51.herokuapp.com/recommend/0bf59bde-f78e-4dd2-a334-5c7f22dfa14d?k=5
```

**Contoh Response:**

```json
{
  "user_id": "0bf59bde-f78e-4dd2-a334-5c7f22dfa14d",
  "recommendations": [
    {
      "user_id": "8c1bd284-e129-4d8d-a610-29ba2806895d",
      "umkm_id": "8c1bd284-e129-4d8d-a610-29ba2806895d",
      "kategori": "Kuliner",
      "model_bisnis": "Dropship",
      "skala": "Kecil",
      "jangkauan": "Regional",
      "similarity_score": 0.863
    },
  ]
}
```

---


## Cara Integrasi dalam Sistem

API ini bersifat **RESTful** dan dapat digunakan dari sistem manapun yang bisa mengirimkan **HTTP GET request**, baik dari sisi frontend maupun backend.

### Frontend (JavaScript/React)

```javascript
fetch("https://umkm-fastapi-heroku-496b36a59a51.herokuapp.com/recommend/USER_ID?k=5")
  .then(res => res.json())
  .then(data => {
    console.log(data.recommendations);
  });
```

---

### Backend (Python)

```python
import requests

user_id = "0bf59bde-f78e-4dd2-a334-5c7f22dfa14d"
k = 5

res = requests.get(f"https://umkm-fastapi-heroku-496b36a59a51.herokuapp.com/recommend/{user_id}?k={k}")
recommendations = res.json()
print(recommendations)
```

---

### Backend (Node.js dengan Hapi.js)

```javascript
const Hapi = require('@hapi/hapi');
const fetch = require('node-fetch');

const init = async () => {
  const server = Hapi.server({
    port: 3000,
    host: 'localhost'
  });

  server.route({
    method: 'GET',
    path: '/recommend/{userId}',
    handler: async (request, h) => {
      const userId = request.params.userId;
      const k = request.query.k || 5;

      try {
        const res = await fetch(`https://umkm-fastapi-heroku-496b36a59a51.herokuapp.com/recommend/${userId}?k=${k}`);
        const data = await res.json();
        return h.response(data).code(200);
      } catch (err) {
        return h.response({ error: 'Failed to fetch recommendation' }).code(500);
      }
    }
  });

  await server.start();
  console.log('Server running on %s', server.info.uri);
};

init();
```

---

### Teknologi Lain

API ini juga bisa digunakan dari:

| Teknologi              | Cara Umum Penggunaan                        |
| ---------------------- | ------------------------------------------- |
| **Vue.js**             | Gunakan `axios.get(...)`                    |
| **Flutter / Dart**     | Gunakan package `http`                      |
| **Android / Java**     | Gunakan `Retrofit` atau `HttpURLConnection` |
| **PHP (Laravel)**      | Gunakan `Http::get()` atau `GuzzleHttp`     |
| **Go**                 | Gunakan `http.Get(...)`                     |
| **Ruby / Rails**       | Gunakan `Net::HTTP.get(...)`                |
| **Java (Spring Boot)** | Gunakan `RestTemplate.getForObject(...)`    |

Selama sistemmu bisa mengakses internet dan mengirim HTTP GET request, maka **API ini bisa diintegrasikan tanpa batasan teknologi**.

---


## Setup Lokal (Opsional)

Untuk menjalankan API ini secara lokal:

```bash
git clone <repository-url>
cd <repository-folder>
python -m venv venv
source venv/bin/activate  # atau venv\Scripts\activate di Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## Dokumentasi Swagger

Setelah API dijalankan (baik di lokal atau di Heroku), dokumentasi interaktif tersedia di:

```
https://umkm-fastapi-heroku-496b36a59a51.herokuapp.com/docs
```

---

## Kontribusi

Kontribusi sangat terbuka untuk:

* Menambahkan fitur filter rekomendasi
* Membuat frontend interface
* Meningkatkan kualitas model

---



