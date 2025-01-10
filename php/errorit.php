<?php
header('Content-Type: text/html');

{
  $virhe_status = $_POST['Status'];
  $virhe_teksti = $_POST['Error'];

  $tiedosto = fopen('../../logs/tulokset.txt', 'w+');

  // Luodaan taulukko (array) datasta ja muutetaan se JSON-muotoon
  $data = array('status' => $virhe_status, 'error' => $virhe_teksti);
  $json_data = json_encode($data);

  fwrite($tiedosto, $json_data);

  fclose($tiedosto);
}
?>
