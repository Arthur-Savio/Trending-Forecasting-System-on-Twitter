import { Component, OnInit } from '@angular/core';
import { ApiService } from "../api.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [ApiService]
})
export class HomeComponent implements OnInit {
  setup = {id:'1', term:'', limit:''};
  constructor(private api: ApiService) { }

  ngOnInit() {
    this.getSetup();
  }

  getSetup = () => {
    this.api.getSetup().subscribe(
      data => {
        var my_data = data;
        this.setup['term'] = my_data[0]['term'];
        this.setup['limit'] = my_data[0]['limit'];
        },
      error => {
        console.log(error);
      }
    )
  }

  updateSetup = () => {
    this.api.updateSetup(this.setup).subscribe(
      data => {
        this.setup = data;
      },
      error => {
        console.log(error);
      }
    )
  }
}
