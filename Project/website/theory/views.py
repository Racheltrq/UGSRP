from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse


from .models import Key


def home(request):
    keys = Key.objects.all()
    print(len(keys))
    return render(request, "home.html", {"keys": keys})


def get_files(key):
    if key.type == "maj":
        files = []
        midiFile = str(key).replace(" ", "") + ".midi"
        pngFile = str(key).replace(" ", "") + ".png"
        files.append(midiFile)
        files.append(pngFile)
    else:
        files = []
        files.append(
            [str(key).replace(" ", "") + "1.midi",
             str(key).replace(" ", "") + "1.png"]
        )
        files.append(
            [str(key).replace(" ", "") + "2.midi",
             str(key).replace(" ", "") + "2.png"]
        )
        files.append(
            [str(key).replace(" ", "") + "3.midi",
             str(key).replace(" ", "") + "3.png"]
        )
    return files


def key_detail(request, id):
    key = get_object_or_404(Key, id=id)
    files = get_files(key)
    return render(request, "key_detail.html", {"key": key, "file": files})


def toggle_common(request, id, state):
    print("state:", state)
    key = Key.objects.get(id=id)
    print("In common1", id, key.common)
    if state == "1":
        print("instate1")
        key.common = True
        key.save()
    else:
        key.common = False
        key.save()

    print("In common2", id, key.common)
    midiFile, pngFile = get_files(key)
    return redirect(reverse("key_detail", args=[id]))
