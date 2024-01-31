import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './component/home/home.component';
import { HeaderComponent } from './component/header/header.component';
import { TrackingComponent } from './component/tracking/tracking.component';
import { DocComponent } from './component/doc/doc.component';
import { TrackingsocketComponent } from './component/trackingsocket/trackingsocket.component';

const routes: Routes = [
  { path: 'home', component : HomeComponent}, 
  { path: 'tracking', component: TrackingComponent},
  { path: 'trackingsocket', component: TrackingsocketComponent},
  { path: 'doc', component: DocComponent},
  { path: '', component : HomeComponent},
  { path: '**', redirectTo: '' } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
