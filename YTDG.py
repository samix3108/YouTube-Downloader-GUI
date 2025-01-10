import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp

def check_link():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira o link do vídeo.")
        return

    try:
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
            global video_title
            video_title = info.get('title', 'Vídeo')
        
        enable_download_options()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar o vídeo: {str(e)}")

def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

def download():
    url = url_entry.get()
    download_type = download_type_var.get()
    quality = quality_var.get()
    save_directory = directory_entry.get()

    if not save_directory:
        messagebox.showwarning("Aviso", "Por favor, escolha um diretório para salvar o arquivo.")
        return

    try:
        ydl_opts = configure_download_options(download_type, quality, save_directory)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        messagebox.showinfo("Sucesso", "Download concluído!")
        clear_url_entry()
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def configure_download_options(download_type, quality, save_directory):
    if download_type == "Áudio":
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{save_directory}/{video_title}.%(ext)s',
        }
    else:
        format_option = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' if quality == "Alta qualidade" else 'worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]/worst'
        return {
            'format': format_option,
            'outtmpl': f'{save_directory}/{video_title}.%(ext)s',
        }

def enable_download_options():
    audio_button.config(state=tk.NORMAL)
    video_button.config(state=tk.NORMAL)
    quality_menu.config(state=tk.NORMAL)
    download_button.config(state=tk.NORMAL)
    directory_button.config(state=tk.NORMAL)

def clear_url_entry():
    url_entry.delete(0, tk.END)
    verify_button.config(state=tk.DISABLED)

def update_buttons(*args):
    verify_button.config(state=tk.NORMAL if url_entry.get() else tk.DISABLED)

root = tk.Tk()
root.title("Downloader de YouTube (by samix3108)")

tk.Label(root, text="Link do vídeo:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

verify_button = tk.Button(root, text="Verificar Link", command=check_link, state=tk.DISABLED)
verify_button.pack()

tk.Label(root, text="Diretório de salvamento:").pack()
directory_entry = tk.Entry(root, width=50)
directory_entry.pack()

directory_button = tk.Button(root, text="Escolher Diretório", command=choose_directory, state=tk.DISABLED)
directory_button.pack()

download_type_var = tk.StringVar(value="Vídeo")
audio_button = tk.Radiobutton(root, text="Áudio", variable=download_type_var, value="Áudio", state=tk.DISABLED)
video_button = tk.Radiobutton(root, text="Vídeo", variable=download_type_var, value="Vídeo", state=tk.DISABLED)
audio_button.pack()
video_button.pack()

tk.Label(root, text="Qualidade:").pack()
quality_var = tk.StringVar(value="Alta qualidade")
quality_menu = tk.OptionMenu(root, quality_var, "Alta qualidade", "Baixa qualidade")
quality_menu.config(state=tk.DISABLED)
quality_menu.pack()

download_button = tk.Button(root, text="Baixar", command=download, state=tk.DISABLED)
download_button.pack()

url_entry.bind("<KeyRelease>", update_buttons)

root.mainloop()
