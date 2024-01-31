import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './component/home/home.component';
import { TrackingComponent } from './component/tracking/tracking.component';
import { DocComponent } from './component/doc/doc.component';
import { HeaderComponent } from './component/header/header.component';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';
import { HttpClientModule } from '@angular/common/http';
import { TrackingsocketComponent } from './component/trackingsocket/trackingsocket.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    TrackingComponent,
    DocComponent,
    HeaderComponent,
    TrackingsocketComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    LeafletModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
