import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Subscription } from 'rxjs';

import { Task } from 'src/app/services/task/task';
import { UiService } from 'src/app/services/ui/ui.service';

@Component({
  selector: 'app-add-task',
  templateUrl: './add-task.component.html',
  styleUrls: ['./add-task.component.css'],
})
export class AddTaskComponent implements OnInit {
  task: string = '';
  day: string = '';
  reminder: boolean = false;

  @Output() onAddTask: EventEmitter<Task> = new EventEmitter();

  showForm: boolean = false;
  subscription: Subscription = new Subscription();

  constructor(private uiService: UiService) {}

  ngOnInit(): void {
    this.subscription = this.uiService
      .getState()
      .subscribe((showForm) => (this.showForm = showForm));
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  onSubmit() {
    const task: Task = {
      text: this.task,
      day: this.day,
      reminder: this.reminder,
    };

    this.onAddTask.emit(task);

    this.task = '';
    this.day = '';
    this.reminder = false;
  }
}
