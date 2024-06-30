import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OGDownloader")
        self.root.geometry("600x300")
        self.root.configure(bg="#f0f0f0")

       
        self.title_label = tk.Label(self.root, text="OGDownloader", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        
        self.url_label = tk.Label(self.root, text="YouTube Video URL'si:", font=("Helvetica", 12), bg="#f0f0f0")
        self.url_label.pack(pady=5)
        self.url_entry = tk.Entry(self.root, width=60, font=("Helvetica", 12))
        self.url_entry.pack(pady=5)

        
        self.download_button = tk.Button(self.root, text="İndir", font=("Helvetica", 12, "bold"), command=self.download_video, bg="#4CAF50", fg="white")
        self.download_button.pack(pady=20)

        
        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.status_label.pack(pady=10)

    def download_video(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Hata", "Lütfen bir YouTube linki giriniz.")
            return

        download_path = filedialog.askdirectory()
        if not download_path:
            messagebox.showerror("Hata", "Lütfen bir indirme dizini seçiniz.")
            return

        try:
            yt = YouTube(url)
            stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
            self.status_label.config(text="İndiriliyor, lütfen bekleyin...")
            stream.download(output_path=download_path)
            self.status_label.config(text="İndirme tamamlandı!")
            messagebox.showinfo("Başarılı", "Video başarıyla indirildi!")
        except Exception as e:
            self.status_label.config(text="")
            messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")


root = tk.Tk()
app = YouTubeDownloaderApp(root)
root.mainloop()
