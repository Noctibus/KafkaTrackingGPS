import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './component/home/home.component';
import { HeaderComponent } from './component/header/header.component';
import { TrackingComponent } from './component/tracking/tracking.component';

const routes: Routes = [
  { path: '', component : HomeComponent},
  { path: 'home', component : HomeComponent}, 
  { path: 'tracking', component: TrackingComponent},
  { path: '**', redirectTo: '' } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
