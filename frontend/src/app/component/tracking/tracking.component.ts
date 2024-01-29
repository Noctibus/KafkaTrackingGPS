import { Component, OnInit } from '@angular/core';
import * as L from 'leaflet';
import { CoordinatesService } from '../../services/coordinates.service';

@Component({
  selector: 'app-tracking',
  templateUrl: './tracking.component.html',
  styleUrl: './tracking.component.scss',
})
export class TrackingComponent implements OnInit {

  machine_ID = 'IP1';
  gpsData: any[] = [];

  private map!: L.Map
  markers: L.Marker[] = [
    L.marker([31.9539, 35.9106]), // Amman
    L.marker([32.5568, 35.8469]) // Irbid
  ];

  constructor(private coordinatesService: CoordinatesService) {}

  ngOnInit(): void {
    this.coordinatesService.getCoordinates(this.machine_ID).subscribe((data: any) => {
      this.gpsData = data;
      console.log(data);
      this.logCoordinates();
    });
  }

  logCoordinates(): void {
    for (const point of this.gpsData) {
      console.log('Latitude:', point.latitude, 'Longitude:', point.longitude);
    }
  }

  // Declare options and layersControl properties
  options = {
    layers: [
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
      }),
    ],
    zoom: 12,
    center: L.latLng(43.27, -0.35),
    maxBounds: L.latLngBounds(L.latLng(43.3, -0.4), L.latLng(43.25, -0.3)), 
    maxBoundsViscosity: 0.8,
    icon: L.icon({
      iconUrl: 'assets/marker-icon.png',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      tooltipAnchor: [16, -28],
      shadowSize: [41, 41]
    })
  };

  layers = [
    L.marker([ 43.27, -0.35])
  ];
  
}