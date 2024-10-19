enum DnaSummaryCreateStatus {
  NotYet = 0, // まだ作成されていない状態
  InProgress = 1, // 作成中
  Completed = 2, // 作成完了
  Failed = 3, // 作成失敗
}

export default DnaSummaryCreateStatus;
