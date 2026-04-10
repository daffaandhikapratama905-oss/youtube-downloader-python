import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import yt_dlp
import os

class YoutubeDownloader(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Input URL
        self.url_input = toga.TextInput(
            placeholder="Tempel link YouTube di sini...",
            style=Pack(padding=(0, 0, 10, 0))
        )

        # Pilihan Format (Dropdown/Selection)
        self.format_select = toga.Selection(
            items=["Video (MP4)", "Audio (MP3)"],
            style=Pack(padding=(0, 0, 10, 0))
        )

        # Tombol Download
        download_btn = toga.Button(
            "Mulai Download",
            on_press=self.handle_download,
            style=Pack(padding=5)
        )

        main_box.add(toga.Label("Masukkan Link:", style=Pack(padding=(0, 5))))
        main_box.add(self.url_input)
        main_box.add(toga.Label("Pilih Format:", style=Pack(padding=(0, 5))))
        main_box.add(self.format_select)
        main_box.add(download_btn)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def handle_download(self, widget):
        url = self.url_input.value
        pilihan = self.format_select.value
        
        if not url:
            self.main_window.error_dialog("Ups!", "Masukkan link dulu ya.")
            return

        # Folder Downloads
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # Logika Pilihan Format
        if pilihan == "Audio (MP3)":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        else:
            # Video MP4 (best)
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.main_window.info_dialog("Berhasil!", f"{pilihan} sudah masuk ke folder Downloads.")
        except Exception as e:
            self.main_window.error_dialog("Gagal", f"Error: {e}")

def main():
    return YoutubeDownloader()