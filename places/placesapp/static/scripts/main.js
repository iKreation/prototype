var onspot = {

	categories:null,
	places: {},
	currentMarker:null,



	initialize: function() {
		
		google.maps.event.addDomListener(window, 'load', this.initGoogleMaps);

		this.getPlaces();

		window.markers = [];

				
	},

	getPlaces: function() {
		var that = this;
		
		$.get('http://localhost:8000/places/0/', function(data) {
			window.onspot.places = data;
			
			//console.log(window.onspot.categories);
		});
	},


	initGoogleMaps: function() {
		google.maps.visualRefresh = true;

		

        console.log("clickedCreate");
		
		var mapOptions = {
	    	zoom: 13,
	    	center: new google.maps.LatLng(40.20346,-8.447212),
	   		mapTypeId: google.maps.MapTypeId.ROADMAP,
	   		mapTypeControl: true,
		    mapTypeControlOptions: {
		        style: google.maps.MapTypeControlStyle.VERTICAL_BAR,
		        position: google.maps.ControlPosition.RIGHT_BOTTOM
		    },
		    panControl: true,
		    panControlOptions: {
		        position: google.maps.ControlPosition.LEFT_CENTER
		    },
		    zoomControl: true,
		    zoomControlOptions: {
		        style: google.maps.ZoomControlStyle.LARGE,
		        position: google.maps.ControlPosition.LEFT_CENTER
		    },
		    scaleControl: true,
		    scaleControlOptions: {
		        position: google.maps.ControlPosition.LEFT_CENTER
		    },
		    streetViewControl: true,
		    streetViewControlOptions: {
		        position: google.maps.ControlPosition.LEFT_CENTER
		    }
	  	};

	  	window.onspotMap = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);

	  	myListener = google.maps.event.addListener(window.onspotMap, 'click', function(event) {
	        window.onspot.placeMarker(event.latLng);
	        //google.maps.event.removeListener(myListener);
	        $("#categories").hide();
	        $("#createForm").show();

	    });

	  	window.onspot.addMarkersByCategories(0);
		
	},


	placeMarker:function(location) {

		window.onspot.removeAllMarkers();
        var marker = new google.maps.Marker({
            position: location,
            map: window.onspotMap,
            draggable: true
        });
        //window.onspotMap.setCenter(location);
        var markerPosition = marker.getPosition();
        window.onspot.currentMarker = location['k'] + ',' + location['A'];
        //populateInputs(markerPosition);
        //google.maps.event.addListener(marker, "drag", function (mEvent) {
           // populateInputs(mEvent.latLng);
    },

	addMarkersByCategories: function() {

		console.log(selectedCategories);


		this.removeAllMarkers(window.onspotMap);

		for(var i = 0; i < selectedCategories.length; i++) {
			if(selectedCategories[i] == 1) {
				for(var j = 0; j < this.places.length; j++) {
					if (this.places[j].category_id-1==i) {
						console.log("adding markers");
						console.log(this.places[i]);
						this.addMarker(this.places[j]);
					};
				}
			}
		}

		var bounds = new google.maps.LatLngBounds();

		for(var i = 0; i < markerBounds.length; i++) {
			bounds.extend(markerBounds[i]);
		}

		window.onspotMap.fitBounds(bounds);

		
	},

	removeAllMarkers: function() {
		this.setAllMap(null);
		markerBounds = [];
	},

	removeCurrentMarker: function() {
		this.setAllMap(null);
		markerBounds = [];
		this.addMarkersByCategories();
	},

	// Sets the map on all markers in the array.
	setAllMap: function(map){
	  for (var i = 0; i < markers.length; i++) {
	    window.markers[i].setMap(map);
	  }
	},

	addMarker: function(obj) {

		var coordsSplited = obj.coordinate.split(',');
		console.log(coordsSplited);
		console.log(obj.title);
		console.log(obj.description);
	  	var myLatlng = new google.maps.LatLng(coordsSplited[0],coordsSplited[1]);

	  	markerBounds.push(new google.maps.LatLng(coordsSplited[0],coordsSplited[1]));
	  	
		var contentString = '<div id="content">'+
	      '<div id="siteNotice">'+
	      '</div>'+
	      '<h1 id="firstHeading" class="firstHeading">' + obj.title + '</h1>'+
	      '<div id="bodyContent">'+
	      '<p><b>' + obj.title + '</b>, ' + obj.description + ' </p>'+
	      '</div>'+
	      '</div>';


	  var marker = new google.maps.Marker({
	      position: myLatlng,
		  map: window.onspotMap,
	      title: obj.title
	  });

	  /*
	  if(obj.id == 0) {
	  	marker.setIcon("http://mapicons.nicolasmollet.com/wp-content/uploads/mapicons/shape-default/color-ff8a22/shapecolor-color/shadow-1/border-dark/symbolstyle-white/symbolshadowstyle-dark/gradient-no/sponge.png");
	  } else if(obj.id == 2) {
	  	marker.setIcon("http://mapicons.nicolasmollet.com/wp-content/uploads/mapicons/shape-default/color-36ff24/shapecolor-color/shadow-1/border-dark/symbolstyle-white/symbolshadowstyle-dark/gradient-no/sponge.png");
	  } else if(obj.id == 1) {
	  	marker.setIcon("http://mapicons.nicolasmollet.com/wp-content/uploads/mapicons/shape-default/color-333333/shapecolor-color/shadow-1/border-dark/symbolstyle-white/symbolshadowstyle-dark/gradient-no/bar_coktail.png");
	  } else if(obj.id == 3) {
	  	marker.setIcon("http://mapicons.nicolasmollet.com/wp-content/uploads/mapicons/shape-default/color-2663ff/shapecolor-color/shadow-1/border-dark/symbolstyle-white/symbolshadowstyle-dark/gradient-no/coffee.png");
	  }
	  */

	  console.log(marker);

	  google.maps.event.addListener(marker, 'click', function() {
	  	if(infowindow) {
	  		console.log("entrou");
	  		infowindow.close();
	  	} 

	  	var infowindow = new google.maps.InfoWindow({
	      content: contentString
	  	});

	  	infowindow.open(onspotMap,marker);

	  	$('#details').html("<h2  style='color:#f3f3f3;'> Detalhes </h2> <h4 style='color:#f3f3f3;'>Nome</h4>" + obj.title + "<h4 style='color:#f3f3f3;'>Descricao</h4>" + obj.description  + "<h4 style='color:#f3f3f3;'>GPS</h4>" + obj.coordinate);
 		$('#details_container').show();
 	  });

	  window.markers.push(marker);
	}
}


$(document).ready(function() {
	var onspotMap;
	onspot.initialize();

});

$