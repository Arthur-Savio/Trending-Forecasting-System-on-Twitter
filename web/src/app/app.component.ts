import { Component, ViewChild } from '@angular/core';
import { ApiService } from "./api.service";
import { LocationsComponent } from "./locations/locations.component";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  @ViewChild("map")
  public mapElement: LocationsComponent;

  constructor(private api: ApiService){
  }

}
