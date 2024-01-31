import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import * as L from 'leaflet';

import { CoordinatesService } from '../../services/coordinates.service';
import { WebsocketService } from '../../services/websocket.service';

import { coordinates } from '../../model/coordinates.model';
import { icon, Marker } from 'leaflet';

import { Subject, takeUntil } from 'rxjs';

const iconRetinaUrl = 'assets/marker-icon-2x.png';
const iconUrl = 'assets/marker-icon.png';
const shadowUrl = 'assets/marker-shadow.png';
const iconDefault = icon({
  iconRetinaUrl,
  iconUrl,
  shadowUrl,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [16, -28],
  shadowSize: [41, 41]
});
Marker.prototype.options.icon = iconDefault;

@Component({
  selector: 'app-trackingsocket',
  templateUrl: './trackingsocket.component.html',
  styleUrls: ['./trackingsocket.component.scss']
})
export class TrackingsocketComponent implements OnInit {
  machine_ID = 'IP1';
  markers: L.Marker[] = [];
  private destroy$ = new Subject<void>();

  constructor(
    private webSocketService: WebsocketService,
    private coordinatesService: CoordinatesService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.webSocketService.connect()
      .pipe(takeUntil(this.destroy$))
      .subscribe((data: any) => {
        const latestGpsData = new coordinates(data.latitude, data.longitude);
        console.log('Latest Coordinates:', latestGpsData);
        this.addMarker(latestGpsData);
        console.log('Markers Array:', this.markers);
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }

  addMarker(coordinates: coordinates): void {
    const newMarker = L.marker([coordinates.latitude, coordinates.longitude], {
      icon: L.icon({
        iconUrl: 'assets/marker-icon.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        tooltipAnchor: [16, -28],
        shadowSize: [41, 41],
      }),
    });
    this.markers.push(newMarker);
    this.layers = this.markers;
  }

  private map!: L.Map;
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
      shadowSize: [41, 41],
    }),
  };

  layers = [L.marker([43.27, -0.35])];
}
