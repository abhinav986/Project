from embed_video.backends import VimeoBackend, detect_backend
import re

class ZenVimeoBackend(VimeoBackend):
    pattern_url = 'https://player.vimeo.com/video/{code}/'
