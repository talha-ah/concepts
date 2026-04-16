import { Component, OnInit } from '@angular/core';

import { Task } from '../../services/task/task';
import { TaskService } from '../../services/task/task.service';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css'],
})
export class TasksComponent implements OnInit {
  tasks: Task[] = [];

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.taskService.getTasks().subscribe((tasks) => (this.tasks = tasks));
  }

  onAddTask(task: Task) {
    task.id = this.tasks.length + 1;
    this.taskService.addTask(task).subscribe(() => this.tasks.push(task));
  }

  onDeleteTask(task: Task): void {
    this.taskService
      .deleteTask(task)
      .subscribe(
        () => (this.tasks = this.tasks.filter((t) => t.id !== task.id))
      );
  }

  onToggleTask(task: Task): void {
    task.reminder = !task.reminder;

    this.taskService.toggleTaskReminder(task).subscribe(() => {
      this.tasks = this.tasks.map((t) => {
        if (task.id === t.id) t = task;
        return t;
      });
    });
  }
}
