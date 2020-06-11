from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect


from .models import Key

def home(request):
    keys = Key.objects.all()
    print(len(keys))
    return render(request, 'home.html', {'keys': keys})

def get_files(key):
    if key.type == 'maj':
        midiFile = str(key).replace(" ", "") + ".midi"
        pngFile = str(key).replace(" ", "") + ".png"
    else:
        midiFile = []
        pngFile = []
        midiFile.append(str(key).replace(" ", "") + "1.midi")
        midiFile.append(str(key).replace(" ", "") + "2.midi")
        midiFile.append(str(key).replace(" ", "") + "3.midi")
        pngFile.append(str(key).replace(" ", "") + "1.png")
        pngFile.append(str(key).replace(" ", "") + "2.png")
        pngFile.append(str(key).replace(" ", "") + "3.png")
    return midiFile, pngFile

def key_detail(request, id):
    try:
        key = Key.objects.get(id = id)
        midiFile, pngFile = get_files(key)
    except Key.DoesNotExist:
        raise Http404('Key not found.')
    return render(request, 'key_detail.html', {
                                                'key': key,
                                                'pngFile': pngFile,
                                                'midiFile': midiFile
                                                })


def common(request, id):
    key = Key.objects.get(id=id)
    print("In common1", id, key.common)
    key.common = True
    key.save()
    print("In common2", id, key.common)
    midiFile, pngFile = get_files(key)
    return redirect('/theory/' + str(id))

def notcommon(request, id):
    key = Key.objects.get(id=id)
    print("In common1", id, key.common)
    key.common = False
    key.save()
    print("In common2", id, key.common)
    midiFile, pngFile = get_files(key)
    return redirect('/theory/' + str(id))
