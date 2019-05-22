import { Component, OnInit } from '@angular/core';
import { ApiService } from "../api.service";


@Component({
  selector: 'app-trending-topics',
  templateUrl: './trending-topics.component.html',
  styleUrls: ['./trending-topics.component.css'],
  providers: [ApiService]
})

export class TrendingTopicsComponent implements OnInit {
  trendingList = []
  constructor(private api: ApiService) { }

  ngOnInit() {
    this.getTrendingTopics();
  }

  getTrendingTopics = () => {
    this.api.getTrendingTopics().subscribe(
      data => {
        this.trendingList = data;
        console.log(this.trendingList)
      },
      error => {
        console.log(error);
      }
    )
  }
}
