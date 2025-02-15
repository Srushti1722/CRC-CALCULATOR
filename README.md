# CRC-CALCULATOR
The CRC Calculator is a tool designed to demonstrate the application of the Cyclic Redundancy Check (CRC) algorithm, a widely-used method for detecting errors in data transmission.





---

# 🚀 CRC Calculator Web App  

🔍 **Ever wondered how errors in digital communication are detected?**  
💡 The **CRC Calculator** is here to **unravel the mystery** behind **Cyclic Redundancy Check (CRC)**—a **powerful algorithm** used in networking, storage, and data transmission to **ensure data integrity**.  

## 🏆 Why This Project?  
In a world driven by **data exchange**, errors happen—whether due to **network glitches**, **hardware faults**, or **interference**. The CRC algorithm acts as a **watchdog**, detecting errors **before they cause problems**.  

This web app lets you **experiment with CRC calculations** in a simple, intuitive interface. Just **input your binary data and generator polynomial**, and let the magic happen! 🎩✨  

## 🎯 Features  
✅ **Web-based Interface** – No need for complex software, just a browser!  
✅ **Real-time CRC Calculation** – Enter data, hit calculate, and get instant results!  
✅ **Error Detection Simulation** – See how CRC helps detect data corruption.  
✅ **User-friendly & Interactive** – Simple, sleek UI with real-time validation.  

## 🛠️ Tech Stack  
🔹 **Frontend**: HTML, CSS, JavaScript  
🔹 **Backend**: Python, Flask  
🔹 **Styling**: CSS for a clean & modern look  

## 🏗️ How It Works  
🔢 **Step 1**: Enter binary data (e.g., `1101011011`)  
🔬 **Step 2**: Provide a generator polynomial (e.g., `1011`)  
⚙️ **Step 3**: The app runs a modulo-2 division and computes the CRC checksum  
📊 **Step 4**: The output displays the **CRC checksum** and the **transmitted frame**  
🔍 **Step 5**: Use CRC to verify if received data is error-free!  

## 🚀 Quick Start  

### 1️⃣ Install & Run Locally  
```bash
git clone https://github.com/Srushti1722/CRC-CALCULATOR.git
cd crc-calculator
pip install flask
python app.py
```
🎯 Open `http://127.0.0.1:5000/` in your browser and start testing!  

### 2️⃣ Example Run  

#### 📝 Input:  
```
Binary Data:  1101011011  
Generator:    1011  
```  

#### ✅ Output:  
```
CRC Checksum:      100  
Transmitted Frame: 1101011011100


```  
![image](https://github.com/user-attachments/assets/09c03cbe-3653-4f61-bcc3-82b9bafe4cf0)

## 🌍 Real-World Uses  
🚀 **Networking:** Detects errors in Ethernet, Wi-Fi, and Bluetooth  
💾 **Storage Devices:** Ensures data integrity in HDDs, SSDs, and USB drives  
🔗 **File Integrity:** CRC verifies compressed files like ZIP & RAR  
📡 **Space Communication:** Used in NASA’s space transmissions to check data accuracy  

## 📌 Future Enhancements  
✨ **Real-time error simulation** – Introduce error injection for better understanding  
📊 **Graphical representation** – Visualize CRC computations step by step  
🔧 **More CRC variations** – Support for different generator polynomials  

## 💡 Who Should Use This?  
🔹 **Students & Learners** – Understand how CRC works with hands-on experience  
🔹 **Developers & Engineers** – Use CRC for error detection in real-world projects  
🔹 **Tech Enthusiasts** – Explore data integrity & networking concepts  

## 👥 Contributors  
👨‍💻 **SRUSHTI**  


## 📜 License  

🔓 **MIT License** – Feel free to use, modify, and contribute!  

🎯 **Let's build a world of error-free data transmission!** 🚀  

