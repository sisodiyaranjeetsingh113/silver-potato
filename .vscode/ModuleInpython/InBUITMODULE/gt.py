from gtts import gTTS
mt="आपसे मिलकर अच्छा लगा!"
lan='hi'
voice=gTTS(text=mt,lang=lan,slow=False)

voice.save("convert.mp3")
print("converted....")
