import { Component, OnInit, inject } from '@angular/core';
import { PostT } from '../../types/PostT';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.component.html',
})
export class HomeComponent implements OnInit {
  httpclient = inject(HttpClient);
  posts: any = [];

  ngOnInit(): void {
    this.httpclient
      .get('http://127.0.0.1:8000/api/v1/posts/')
      .subscribe((data: any) => {
        console.log(data);
        this.posts = data.data;
      });
  }
}
