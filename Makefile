render:
	manim -pqh 1.py MyScene --save_sections -w

posters:
	cd media/videos/1/1080p60/sections/ && for f in MyScene_*.mp4; do ffmpeg -i "$$f" -frames:v 1 "$${f%.mp4}.png"; done
