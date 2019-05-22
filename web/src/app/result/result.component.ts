import { Component, OnInit } from '@angular/core';
import { ApiService } from "../api.service";


@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css'],
  providers: [ApiService]
})
export class ResultComponent implements OnInit {
  selectedTweets = [];
  constructor(private api: ApiService) { }

  ngOnInit() {
    this.getSelectedTweets();
  }
  
  getSelectedTweets = () => {
    this.api.getAllSelectedTweets().subscribe(
      data => {
        this.selectedTweets = data;
      },
      error => {
        console.log(error);
      }
    )
  }

}
