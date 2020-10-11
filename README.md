<h2>Perfect-Pause</h2>
<p>Computer Vision based attention monitoring  system to aid your movie-watching experience.Automatically pause movies/videos using Computer Vision.</p>
<h3>An Overview</h3>
<p>Our aim is to develop a robust human attention monitoring system based on Computer Vision which will work in harmony with VLC media player, prompting it to execute actions such as pause/play depending on whether the user is paying attention to his monitor or not.</p>
<h3>Why is it useful?</h3>
<ul>
  <li>Make sure that the video/movie keeps playing only when the user is watching.</li>
  <li>Pause the video/movie when the user is unattentive or is not watching.</li>
</ul>
<h3>Example situations where our model will be useful :</h3>
<ul>
  <li>Falling asleep.</li>
  <li>Attend a call.</li>
  <li>Emergency chore.</li>
  <li>Getting called to carry the groceries. from the car.</li>
</ul>
<h3>The Approach</h3>
<p>We are using openCV’s Haar Cascades determine the ROI (region of interest) and process the inference, all of which takes milliseconds and requires minimal computing power.</p>
<h3>What exactly is a Haar-cascade?</h3>
<ul>
  <li>Haar Cascade is a machine learning object detection algorithm used to identify objects in an image or video and based on the concept of ​​ features proposed by Paul Viola and Michael Jones.</li>
  <li>It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.</li>
</ul>
<h3>Integrating VLC Media player:</h3>
<p>We are using a python package called vlc to bridge the gap between Computer-Vision and VLC media player.
<img src="https://user-images.githubusercontent.com/53506835/95672355-bf3b6f80-0bbd-11eb-8fff-c7f4ef6a38ec.png">
<h3>Is it safe?</h3>
<p>Our solution does not store or upload any data, it captures frames from the webcam and deletes the frame as soon as it computes the inference.
</p>
<h3>Contributors</h3>
<ul>
  <li>Siddharth Cilamkoti</li>
  <li>Mainak Deb</li>
  <li>Rishab Mudliar</li>
  <li>Giwansh Aryan</li>
  <li>Sanjay Thiyagarajan</li>
  <li>Navneet Kumar Singh</li>
 </ul>
