# Note Identifier

### Summary

This project is meant to be the beginnings of a tab producing program, i.e. a sound file, like an mp3, is given to the program, and a guitar tab is created with reasonable accuracy. The point of this project is to allow for live recordings or more obsure songs to be easily transcribed without the use of paid software, which often creates sheet music rather than guitar tabs. 

### Difficulties
A major difference between sheet music and guitar tabs are specifying the exact frets based on the physical capabilites of a guitarist. Simply put, sheet music only shows the note of the song, which occurs at multiple different frets on a guitar, so a guitar tab must consider whether the previously played notes or future notes are reachable from each of the frets. If most of the song is played around the 10th fret, a new note added to the tab ought to be placed in the same area, rather than at the 1st or 2nd fret, even if the frequencies played would be the same.

Another major difficulty is identifying the bpm of the recording, in order to best analyze the music. There may exist tools online that can easily do this, but it will definitely produce certain hangbacks when analyzing entire songs

Finally the difference between sustained and repeated notes may prove difficult. A note may last for more than 1 beat, which would show up in each of the sections of frequencies, the same as repeated notes, so the loudness of certain frequencies would need to be looked at as well. A repeated note would be louder than a sustained note fadng away.

### Current workings

Currently I am working on being able to import an audio file that contains a single frequency being played, and then identifying the frequency

