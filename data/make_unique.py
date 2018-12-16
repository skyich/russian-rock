{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "UnicodeDecodeError",
     "evalue": "'charmap' codec can't decode byte 0x98 in position 122: character maps to <undefined>",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnicodeDecodeError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-a5e927ec844b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mstr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'music2.txt'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'r'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\encodings\\cp1251.py\u001b[0m in \u001b[0;36mdecode\u001b[1;34m(self, input, final)\u001b[0m\n\u001b[0;32m     21\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mIncrementalDecoder\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcodecs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mIncrementalDecoder\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     22\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mdecode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfinal\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 23\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mcodecs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcharmap_decode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mdecoding_table\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     24\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     25\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mStreamWriter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mCodec\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mcodecs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mStreamWriter\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mUnicodeDecodeError\u001b[0m: 'charmap' codec can't decode byte 0x98 in position 122: character maps to <undefined>"
     ]
    }
   ],
   "source": [
    "str = open('music2.txt', 'r').read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data1.split( \"\\n\\n\" )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
