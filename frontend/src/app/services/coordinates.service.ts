import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CoordinatesService {

  private baseFastAPIurl = 'http://127.0.0.1:8000/test';

  constructor(private http: HttpClient) { }

  getCoordinates(): Observable<any> {
    return this.http.get(this.baseFastAPIurl);
  }
}
