import { Component, OnInit, ViewChild, ElementRef, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiService } from '../api.service';

declare var L: any;

@Component({
  selector: 'app-locations',
  templateUrl: './locations.component.html',
  styleUrls: ['./locations.component.css']
})
export class LocationsComponent implements OnInit {
  constructor(private api: ApiService) { }

  ngOnInit() {
    this.getLocations();
  }

  getLocations = () => {
    this.api.getLocations().subscribe(
      data => {
        this.loadMap(data);
      },
      error => {
        console.log(error);
      }
    )
  }

  loadMap(locations) {
    var myStyle = {
      radius: 3,
      fillColor: "red",
      color: "red",
      weight: 1,
      opacity: 1,
      fillOpacity: 1
    };

    var mytiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    });
    var map = L.map('map');

    for(let i of locations){
      L.circleMarker([i['latitude'], i['longitude']], myStyle).addTo(map);
    }

    map.addLayer(mytiles).setView([0, 0], 2);
  }
}
