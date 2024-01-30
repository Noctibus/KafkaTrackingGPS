import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { io, Socket } from 'socket.io-client';

@Injectable({
  providedIn: 'root'
})
export class WebsocketService{
  private socket: Socket;

  constructor() {this.socket = io('http://localhost:8000/ws');}

  connectToWebSocket(): Observable<any> {
    return new Observable<any>((observer) => {
      this.socket.on('message', (data: any) => {
        observer.next(data);
      });
      return () => {
        this.socket.disconnect();
      };
    });
  }
}
