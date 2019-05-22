import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import set = Reflect.set;

@Injectable({
  providedIn: 'root'
})

export class ApiService {
  baseurl = "http://localhost:8000";
  httpHeaders = new HttpHeaders({'Content-Type':'application/json'})

  constructor(private http: HttpClient) { }

  getAllSelectedTweets(): Observable<any>{
    return this.http.get(this.baseurl + '/selected_tweets/', {headers: this.httpHeaders});
  }

  getTrendingTopics(): Observable<any> {
    return this.http.get(this.baseurl + '/trending/', {headers: this.httpHeaders});
  }

  getSetup(): Observable<any>{
    return this.http.get(this.baseurl + '/setup/', {headers: this.httpHeaders});
  }

  updateSetup(setup): Observable<any>{
    const body = {term:setup.term, limit:setup.limit};
    return this.http.put(this.baseurl + '/setup/1/', body, {headers:this.httpHeaders});
  }
  
  getLocations(): Observable<any>{
    return this.http.get(this.baseurl + '/locations/', {headers: this.httpHeaders});
  }
}
