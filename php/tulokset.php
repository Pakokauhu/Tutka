<?php
header('Content-Type: text/html');
{
  $tila = $_POST['Status'];
  $leveysaste = $_POST['Lat'];
  $pituusaste = $_POST['Lon'];
  $tarkkuus = $_POST['Acc'];
  $korkeus = $_POST['Alt'];
  $suunta = $_POST['Dir'];
  $nopeus = $_POST['Spd'];

  $data = array(
    'tila' => $tila,
    'leveysaste' => $leveysaste,
    'pituusaste' => $pituusaste,
    'tarkkuus' => $tarkkuus,
    'korkeus' => $korkeus,
    'suunta' => $suunta,
    'nopeus' => $nopeus);

  $json_data = json_encode($data);

  $tiedosto = fopen('../../logs/tulokset.txt', 'w+');
  fwrite($tiedosto, $json_data);
  fclose($tiedosto);
}
?>
