import { Component, OnInit, inject } from '@angular/core';
import { PostT } from '../../types/PostT';
import { HttpClient } from '@angular/common/http';
import { NewpostComponent } from '../components/newpost/newpost.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [NewpostComponent],
  templateUrl: './home.component.html',
})
export class HomeComponent implements OnInit {
  httpclient = inject(HttpClient);
  posts: any = [];

  ngOnInit(): void {
    this.httpclient
      .get('http://127.0.0.1:8000/api/v1/posts/')
      .subscribe((data: any) => {
        this.posts = data.data;
      });
  }
}
