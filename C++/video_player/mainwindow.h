#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtMultimedia>
#include <QtMultimediaWidgets>
#include <QtCore>
#include <QtWidgets>
#include <QtGui>
#include <QAudio>
#include <QAudioOutput>



QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void durationChanged(qint64 Duration);
    void positionChanged(qint64 Duration);


    void on_horizontalSlider_duration_valueChanged(int value);


    void on_pushButton_play_pause_clicked();

    void on_pushButton_stop_clicked();

    void on_pushButton_volume_clicked();

    void on_horizontalSlider_volume_valueChanged(int value);

    void on_actionOpen_triggered();

    void on_pushButton_seek_backward_clicked();

    void on_pushButton_seek_forward_clicked();

    void onDurationChanged(qint64 duration);
    void onPositionChanged(qint64 position);

private:
    Ui::MainWindow *ui;
    QMediaPlayer *Player;
    QVideoWidget *Video;
     QAudioOutput *audioOutput;

    qint64 mDuration;
    bool IS_Pause = true;
    bool IS_Muted = false;

    void updateDuration(qint64 Duration);


};
#endif // MAINWINDOW_H
