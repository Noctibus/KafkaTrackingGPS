import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CoordinatesService {

  private baseFastAPIurl = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  getCoordinates(machine_ID : string): Observable<any> {
    const url = `${this.baseFastAPIurl}/fake-gps/${machine_ID}`;
    return this.http.get(this.baseFastAPIurl + 'fake-gps/IP1');
  }
}
