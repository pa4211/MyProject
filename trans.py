import whisper
model = whisper.load_model("medium")
print(model)
#out = model.transcribe("/Users/poojaagarwal/Downloads/audio new.m4a", language='en', verbose=True)
#print(out['text'])