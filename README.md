# Summary
### Uses Google Pegasus to summarize a body of text
https://github.com/google-research/pegasus

<hr>

Sample text used is from Wikipedia:

https://en.wikipedia.org/wiki/Automatic_summarization

<hr>

Takes a txt as argument and uses Pegasus to provide a summary of the input text.
<br>
Open a command prompt and `cd` to a new directory of your choosing:

(optional; recommended) Create a virtual environment with:
```
python -m venv "venv"
venv\Scripts\activate
```

To install do:
```
git clone https://github.com/vluz/sdnano.git
cd Summary
pip install -r requirements.txt
```

On first run it will download several models.
<br>
It will take quite some time, both on reqs above and on first run.
<br>
Please allow it time to finish.
<br>
All runs after the first are then faster to load.

To run do:<br>
`python summary.py` for the fully functional cli version**

Do not use for production, untested.
