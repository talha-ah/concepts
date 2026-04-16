import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';

import { UiService } from 'src/app/services/ui/ui.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
})
export class HeaderComponent implements OnInit {
  title = 'Tasks Tracker';
  showForm: boolean = false;
  subscription: Subscription = new Subscription();

  constructor(private uiService: UiService, private router: Router) {}

  ngOnInit(): void {
    this.subscription = this.uiService
      .getState()
      .subscribe((showForm) => (this.showForm = showForm));
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  onAddClick() {
    this.uiService.toggleState();
  }

  checkRoute(route: string) {
    return this.router.url === route;
  }
}
