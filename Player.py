import os
from pygame import mixer
import Model
from tkinter import filedialog
from mutagen.mp3 import MP3
class Player:
    def __init__(self):
        mixer.init()
        self.my_model=Model.model()

    def get_db_status(self):
        return self.my_model.get_db_status()


    def close_player(self):
        mixer.music.stop()
        self.my_model.close_db_connection()


    def set_volume(self,volume_level):
        mixer.music.set_volume(volume_level)

    def set_time(self,set_time):
        mixer.music.set_pos(set_time)


    def add_song(self):
        song_path_tuple=filedialog.askopenfilenames(title="choose your song",filetype=[("mp3 files","*.mp3")])
        if song_path_tuple=="":
            return
        song_name_list=[]
        for x in song_path_tuple:
            song_name=os.path.basename(x)
            self.my_model.add_song(song_name,x)
            song_name_list.append(song_name)
        return song_name_list



    def remove_song(self,song_name):
        self.my_model.remove_song(song_name)


    def get_song_length(self,song_name):
        self.sp=self.my_model.get_song_path(song_name)
        self.audio_tag=MP3(self.sp)
        song_length=self.audio_tag.info.length
        return song_length

    def get_song_count(self):
        return self.my_model.get_song_count()


    def play_song(self):
        mixer.quit()
        mixer.init(frequency=self.audio_tag.info.sample_rate)
        mixer.music.load(self.sp)
        mixer.music.play()


    def stop_song(self):
        mixer.music.stop()


    def pause_song(self):
        mixer.music.pause()


    def unpause_song(self):
        mixer.music.unpause()


    def add_song_to_favourite(self,song_name):
        song_path=self.my_model.get_song_path(song_name)
        result=self.my_model.add_song_to_favourites(song_name,song_path)
        return result


    def load_song_from_favourites(self):
        result=self.my_model.load_song_favourites()
        return result,self.my_model.song_dict


    def remove_songs_from_favourites(self,song_name):
        result=self.my_model.remove_song_from_favourites(song_name)
        return result













