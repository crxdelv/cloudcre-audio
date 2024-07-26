### cloudcre-audio :minidisc:

cloudcre-audio (formerly known as creytm) is an open-source backend REST API of cloudcre for streaming audio files retrieved from YT Music.

Due to pytube's issue, it uses [pytubefix](https://pypi.org/project/pytubefix/) instead to download the MPEG-3 audio streams.

### Usage :books:

```html
<audio src="https://cloudcre-audio.vercel.app/id" controls="">
```

If you want the server to send a `Content-Disposition` header, add `/dispose/` and the MPEG-3 filename at the end.

```html
<a href="https://cloudcre-audio.vercel.app/dispose/id/filename.mp3">Download this audio</a>
```

### Quality :headphones:

Due to Vercel's response limitation, cloudcre selects the lowest quality.

**Quality:** 32kpbs&ast; <br>
**Mime Type:** audio/mpeg <br>
**Progressive:** No <br>

&ast; Depends on the audio file. It can be higher than the standard.

### Limit :construction:

|   | Recommended | Somehow works | Will not work |
|:-:|:-:|:-:|:-:|
| **Duration** | 5 minutes and below | 6 minutes to 12 minutes | 13 minutes and above |
| **Size** | 1MB and below | 2MB to 3MB | 4MB above |

### Latency :hourglass_flowing_sand:

| Duration | Latency |
|:--------:|:-------:|
| 1-7 minutes | 1-3 seconds |
| 7-10 minutes | 2-5 seconds |
| 10+ minutes | 4-7+ seconds (prediction) |

### Deploy your own :rocket:

To deploy your own server, fork this repository.

```sh
git clone https://github.com/creuserr/cloudcre-audio.git
```

Add some adjustments, and deploy it.

### Disclaimer :balance_scale:

cloudcre-audio does not host any files and solely uses third-party library **pytubefix**. I am not liable for any copyright infringements.
