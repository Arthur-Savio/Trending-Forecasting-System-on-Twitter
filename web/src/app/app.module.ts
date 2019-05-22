import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { NavbarComponent } from './navbar/navbar.component';
import { ResultComponent } from './result/result.component';

import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { TrendingTopicsComponent } from './trending-topics/trending-topics.component';
import { LocationsComponent } from './locations/locations.component';

const appRoutes: Routes = [
  { path: 'home', component: HomeComponent},
  { path: 'result', component: ResultComponent },
  { path: 'trending-topics', component:TrendingTopicsComponent },
  { path: 'locations', component: LocationsComponent },
  { path: '', redirectTo: '/home', pathMatch:'full' },
];


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    ResultComponent,
    HomeComponent,
    TrendingTopicsComponent,
    LocationsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot(
      appRoutes,
    )
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
