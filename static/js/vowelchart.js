var vowels_formants_list = {'data':[],'labels':[]}


var stat_text = document.getElementById("stat_text");

var soundFile;

function setup(){
// create an audio in

  mic = new p5.AudioIn();
    // users must manually enable their browser microphone for recording to work properly!
  mic.start();
	// create a sound recorder
  recorder = new p5.SoundRecorder();

  // connect the mic to the recorder
  recorder.setInput(mic);
  // create an empty sound file that we will use to playback the recording
  soundFile = new p5.SoundFile();

  console.log(soundFile);




}

function startRecord() {
	if (getAudioContext().state !== 'running') {
    getAudioContext().resume();
	}
  
  // use the '.enabled' boolean to make sure user enabled the mic (otherwise we'd record silence)
  if (mic.enabled) {
    // Tell recorder to record to a p5.SoundFile which we will use for playback
    recorder.record(soundFile);
    stat_text.textContent = "Recording...";

  }
}

function stopRecord(){
	
	recorder.stop(); // stop recorder, and send the result to soundFile
	stat_text.textContent = "Recording stopped";
  newBuf = soundFile.buffer.getChannelData(0);
  buf = [newBuf];
  soundFile.setBuffer(buf);
}

function playRecord(){
	stat_text.textContent = "Playing Recording...";
	soundFile.play(); // play the result!
}

function addData(chart, label, data){
    chart.data.labels = label;
    chart.data.datasets[0].data = data;
    chart.update();

}

function removeData(chart, label, data) {

    chart.data.labels = [];
    chart.data.datasets.forEach((dataset) => {
        dataset.data = [];
    });
    chart.update();
}

