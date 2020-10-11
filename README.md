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
