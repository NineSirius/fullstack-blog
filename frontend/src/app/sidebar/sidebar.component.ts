import { Component } from '@angular/core';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [],
  templateUrl: './sidebar.component.html',
})
export class SidebarComponent {
  links = [
    {
      label: 'Главная',
      href: '/',
      icon: '',
    },
    {
      label: 'Друзья',
      href: '/friends',
      icon: '',
    },
  ];
}
