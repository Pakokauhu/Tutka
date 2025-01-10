<?php
header('Content-Type: text/html');

{
  $alusta = $_POST['Ptf'];
  $selain = $_POST['Brw'];
  $ytimet = $_POST['Cc'];
  $muisti = $_POST['Ram'];
  $valmistaja = $_POST['Ven'];
  $renderointi = $_POST['Ren'];
  $korkeus = $_POST['Ht'];
  $leveys = $_POST['Wd'];
  $kayttis = $_POST['Os'];

  function haeKayttajanIP()
  {
    if (isset($_SERVER["HTTP_CF_CONNECTING_IP"]))
    {
      $_SERVER['REMOTE_ADDR'] = $_SERVER["HTTP_CF_CONNECTING_IP"];
      $_SERVER['HTTP_CLIENT_IP'] = $_SERVER["HTTP_CF_CONNECTING_IP"];
    }
    $asiakas = @$_SERVER['HTTP_CLIENT_IP'];
    $valitys = @$_SERVER['HTTP_X_FORWARDED_FOR'];
    $etainen = $_SERVER['REMOTE_ADDR'];

    if(filter_var($asiakas, FILTER_VALIDATE_IP))
    {
        $ip = $asiakas;
    }
    elseif(filter_var($valitys, FILTER_VALIDATE_IP))
    {
        $ip = $valitys;
    }
    else
    {
        $ip = $etainen;
    }
    return $ip;
  }

  $ip = haeKayttajanIP();

  $data = array('platform' => $alusta,
  'browser' => $selain,
  'cores' => $ytimet,
  'ram' => $muisti,
  'vendor' => $valmistaja,
  'render' => $renderointi,
  'ip' => $ip,
  'ht' => $korkeus,
  'wd' => $leveys,
  'os' => $kayttis);

  $json_data = json_encode($data);

  $tiedosto = fopen('../../logs/info.txt', 'w+');
  fwrite($tiedosto, $json_data);
  fclose($tiedosto);
}
