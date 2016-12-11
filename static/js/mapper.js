 

    var locations = [
  {% get_locations %}
];
   
 
var geocoder;
var map;
var bounds = new google.maps.LatLngBounds();
google.maps.event.addDomListener(window, "load", initialize);
function initialize() {
  map = new google.maps.Map(
    document.getElementById("map_canvas"), {
      center: new google.maps.LatLng(44.986656, -93.258133),
      zoom: 3,
      panControl: true,
      zoomControl: true,
      zoomControlOptions: {
        position: google.maps.ControlPosition.LEFT_BOTTOM },

      mapTypeControl: true,
      /*scaleControl: true,*/
      streetViewControl: false,
      overviewMapControl: true,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
  geocoder = new google.maps.Geocoder();

    for (i = 0; i < locations.length; i++) { 
  /*for (i = 0; i < 1; i++) { */
     var title = locations[i][0];
     var address = locations[i][6];
     var url = locations[i][3];
     var state = locations[i][4];
     var contact = locations[i][5];
     var city = locations[i][7];
      
     
      

     var marker = new google.maps.Marker({
          icon: 'http://intersure.tmcmarkets.com/wp-content/uploads/2015/01/GoogleMapsPin.png',
          map: map,
          /*position: google.maps.LatLng(locations[i][1][0],locations[i][1][1]),*/
          position:  new google.maps.LatLng(locations[i][1], locations[i][2]),
          /* position:  locations[i][1] */
          state: state,
          title: title,
          animation: google.maps.Animation.DROP,
          address: address, 
          url: url
        })
        infoWindow(marker, map, state,title, address, url,contact,city);
        bounds.extend(marker.getPosition());
        /*map.fitBounds(bounds);*/


    /*geocodeAddress(locations, i);*/
  }
}

/*
google.maps.event.addDomListener(window, "load", initialize);

function geocodeAddress(locations, i) {
  var title = locations[i][0];
  var address = locations[i][1];
  var url = locations[i][2];
  geocoder.geocode({
      'address': locations[i][1]
    },

    function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        
        var marker = new google.maps.Marker({
          icon: 'http://maps.google.com/mapfiles/ms/icons/blue.png',
          map: map,
          position: results[0].geometry.location,
          title: title,
          animation: google.maps.Animation.DROP,
          address: address,
          url: url
        })
        infoWindow(marker, map, title, address, url);
        bounds.extend(marker.getPosition());
        map.fitBounds(bounds);
      } else {
        alert("geocode of " + address + " failed:" + status);
      }
    });
} */

function infoWindow(marker, map, state,title, address, url,contact,city) {
  google.maps.event.addListener(marker, 'click', function() {
    var html = "<div><h3>"+ state+"<br>" + title + "</h3><p>" + contact + "<br>"+address+"<br>"+city+"</div><a target='_blank'  href='" + 
                url + "'>View Website</a></p></div>";
    iw = new google.maps.InfoWindow({
      content: html,
      maxWidth: 550
    });
    iw.open(map, marker);
  });
}

function createMarker(results) {
  var marker = new google.maps.Marker({
    icon: 'http://intersure.tmcmarkets.com/wp-content/uploads/2015/01/GoogleMapsPin.png',
    map: map,
    position: results[0].geometry.location,
    title: title,
    animation: google.maps.Animation.DROP,
    address: address,
    url: url
  })
  bounds.extend(marker.getPosition());
  map.fitBounds(bounds);
  infoWindow(marker, map,state, title, address, url,contact,city);
  return marker;
}
      
    

