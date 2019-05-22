import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
  providers: [ApiService]
})
export class NavbarComponent implements OnInit {

  constructor(private api: ApiService) { }

  ngOnInit() {
  }

}
