export class Editor {
  public text: string = "";
  private history: string[] = [];
  private historyPosition: number = -1;

  constructor(public id: string) {}

  private historyPush(text: string): void {
    this.history[++this.historyPosition] = text;
  }

  public write(text: string): void {
    this.historyPush(this.text + text);
    this.text += text;
  }

  public clear(): void {
    this.text = "";
  }

  public undo(): void {
    if (this.historyPosition === 0 ) {
      this.text = this.history[0];
    } else {
      this.text = this.history[--this.historyPosition];
    }
  }

  public redo(): void {
    if (this.historyPosition === this.history.length - 1 ) {
      this.text = this.history[this.historyPosition];
    } else {
      this.text = this.history[++this.historyPosition];
    }
  }
}
